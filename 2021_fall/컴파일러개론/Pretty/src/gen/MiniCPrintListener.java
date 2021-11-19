package gen;

import org.antlr.v4.runtime.tree.ParseTreeProperty;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class MiniCPrintListener extends MiniCBaseListener{
    String indent = ""; //인덴트를 위한 함수
    ParseTreeProperty<String> newTexts = new ParseTreeProperty<>();
    public boolean isBinaryOperation(MiniCParser.ExprContext ctx) {
        return ctx.getChildCount()==3 && ctx.IDENT()==null;
    }
    public boolean isUnaryOperation(MiniCParser.ExprContext ctx) {
        return ctx.getChildCount()==2 && ctx.getChild(0)!=ctx.expr();
    }
    public boolean startsWithIdent(MiniCParser.ExprContext ctx) {
        return ctx.IDENT() != null;
    }
    public boolean isBracket(MiniCParser.ExprContext ctx) {
        return ctx.getChildCount()==3 && ctx.getChild(0).getText().equals("(") && ctx.getChild(2).getText().equals(")");
    }
    @Override
    public void exitProgram(MiniCParser.ProgramContext ctx) {
        String program = "";
        for (int i = 0; i < ctx.getChildCount(); i++) {
            newTexts.put(ctx, ctx.decl(i).getText()); //ParseTree인 newText에 decl을 넣음
            program += newTexts.get(ctx.getChild(i)); // ctx의 child에 들어갔다가 나오면서 출력
        }
        System.out.println(program);
        File file = new File(String.format("[HW3]201702007.c")); // 본인 학번으로 변경해주세요.
        try {
            FileWriter fw = new FileWriter(file);
            fw.write(program);
            fw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    @Override
    public void exitDecl(MiniCParser.DeclContext ctx) {
        newTexts.put(ctx, newTexts.get(ctx.getChild(0)));
    }
    @Override
    public void exitVar_decl(MiniCParser.Var_declContext ctx) {
        String s1 = newTexts.get(ctx.type_spec());
        String s2 = ctx.IDENT().getText();
        String s3 = null;
        switch(ctx.getChildCount()) {
            case 3:
                newTexts.put(ctx,s1+" "+s2+";\n");
                break;
            case 5:
                s3 = ctx.LITERAL().getText();
                newTexts.put(ctx,s1+" "+s2+" = "+s3+";\n");
                break;
            case 6:
                s3 = ctx.LITERAL().getText();
                newTexts.put(ctx,s1+" "+s2+"["+s3+"]"+";\n");
                break;
        }
    }
    @Override
    public void exitType_spec(MiniCParser.Type_specContext ctx) {
        newTexts.put(ctx, ctx.getChild(0).getText());
    }
    @Override
    public void exitFun_decl(MiniCParser.Fun_declContext ctx) {
        String s1 = newTexts.get(ctx.type_spec());
        String s2 = ctx.IDENT().getText();
        String s3 = newTexts.get(ctx.params());
        String s4 = newTexts.get(ctx.compound_stmt());
        newTexts.put(ctx, s1+" "+s2+"("+s3+")"+"\n"+s4+"\n");
    }
    @Override
    public void exitParams(MiniCParser.ParamsContext ctx) {
        if(ctx.getChildCount()>0) {
            List<MiniCParser.ParamContext> params = ctx.param();
            String[] temp = new String[params.size()];
            if(params.size()>0) {
                for(int i=0; i<params.size(); i++) {
                    temp[i] = newTexts.get((params.get(i)));
                }
                newTexts.put(ctx, String.join(", ", temp));
            }
            else {
                newTexts.put(ctx, ctx.VOID().getText());
            }
        }
        else {
            newTexts.put(ctx, "");
        }
    }
    @Override
    public void exitParam(MiniCParser.ParamContext ctx) {
        String s1 = newTexts.get(ctx.type_spec());
        String s2 = ctx.IDENT().getText();
        if(ctx.getChildCount()==2) {
            newTexts.put(ctx, s1+" "+s2);
        }
        else {
            newTexts.put(ctx, s1+" "+s2+"[]");
        }
    }
    @Override
    public void exitStmt(MiniCParser.StmtContext ctx) {
        newTexts.put(ctx, newTexts.get(ctx.getChild(0)));
    }
    @Override
    public void exitExpr_stmt(MiniCParser.Expr_stmtContext ctx) {
        newTexts.put(ctx, newTexts.get(ctx.expr())+";");
    }
    @Override
    public void exitWhile_stmt(MiniCParser.While_stmtContext ctx) {
        String s1 = ctx.WHILE().getText();
        String s2 = newTexts.get(ctx.expr());
        String s3 = newTexts.get(ctx.stmt());
        newTexts.put(ctx, s1+" "+"("+s2+")"+"\n"+s3);
    }
    @Override
    public void enterCompound_stmt(MiniCParser.Compound_stmtContext ctx) {
        indent += "...."; //인덴트 추가
    }
    @Override
    public void exitCompound_stmt(MiniCParser.Compound_stmtContext ctx) {
        String[] local_decls; //local_decls 배열
        String[] stmts; //stmts 배열
        //자식들을 읽어서 모두 배열에 저장
        if(ctx.local_decl()!=null) {
            local_decls = new String[ctx.local_decl().size()];
            for(int i=0; i<local_decls.length; i++) {
                local_decls[i] = indent+newTexts.get(ctx.local_decl(i));
            }
        } else {
            local_decls = new String[] {""};
        }
        if(ctx.stmt()!=null) {
            stmts = new String[ctx.stmt().size()];
            for(int i=0; i<stmts.length; i++) {
                stmts[i] = indent+newTexts.get(ctx.stmt(i));
            }
        } else {
            stmts = new String[] {""};
        }
        //arraycopy 메소드를 통해 한 배열에 합침
        String[] result = new String[local_decls.length + stmts.length];
        System.arraycopy(local_decls, 0, result, 0, local_decls.length);
        System.arraycopy(stmts, 0, result, local_decls.length, stmts.length);
        //join 메소드를 통해 라인 사이 사이에 개행을 더해줌
        String toAdd = result.length==0 ? "" : String.join("\n", result);
        String tempIndent = indent.substring(0, indent.length()-4);
        newTexts.put(ctx, tempIndent+"{\n"+toAdd+"\n"+tempIndent+"}");
        indent = indent.substring(0, indent.length()-4);
    }
    @Override
    public void exitLocal_decl(MiniCParser.Local_declContext ctx) {
        String s1 = newTexts.get(ctx.type_spec());
        String s2 = ctx.IDENT().getText();
        String s3 = null;
        switch(ctx.getChildCount()) {
            case 3:
                newTexts.put(ctx, s1 + " " + s2 + ";");
                break;
            case 5:
                s3 = ctx.LITERAL().getText();
                newTexts.put(ctx, s1 + " " + s2 + " = " + s3 + ";");
                break;
            case 6:
                s3 = ctx.LITERAL().getText();
                newTexts.put(ctx, s1 + " " + s2 + "[" + s3 + "]" + ";");
                break;
        }
    }
    @Override
    public void exitIf_stmt(MiniCParser.If_stmtContext ctx) {
        String s1 = newTexts.get(ctx.expr());
        String s2 = newTexts.get(ctx.stmt(0));
        if(ctx.getChildCount()>5) {
            String s3 = newTexts.get(ctx.stmt(1));
            newTexts.put(ctx, "if"+" "+"("+s1+")"+"\n"+s2+"\n"+"else"+"\n"+s3);
        }
        else if(ctx.stmt(0).expr_stmt()!=null) {
            newTexts.put(ctx, "if"+" "+"("+s1+") "+s2);
        }
        else {
            newTexts.put(ctx, "if"+" "+"("+s1+")"+"\n"+s2);
        }
    }
    @Override
    public void exitReturn_stmt(MiniCParser.Return_stmtContext ctx) {
        if(ctx.getChildCount()>2) {
            String temp = newTexts.get(ctx.expr());
            newTexts.put(ctx, "return" + " "+ temp + ";");
        }
        else {
            newTexts.put(ctx, "return;");
        }
    }
    @Override
    public void exitExpr(MiniCParser.ExprContext ctx) {
        if(isBracket(ctx)) {
            String temp = newTexts.get(ctx.expr(0));
            newTexts.put(ctx, "("+temp+")");
        }
        else if(isBinaryOperation(ctx)) {
            System.out.println("b1: " + ctx.getText());
            String s1 = newTexts.get(ctx.expr(0));
            String s2 = newTexts.get(ctx.expr(1));
            String s3 = ctx.getChild(1).getText();
            newTexts.put(ctx, s1+" "+s3+" "+s2);
        }
        else if(isUnaryOperation(ctx)) {
            String s1 = ctx.getChild(0).getText();
            String s2 = newTexts.get(ctx.expr(0));
            newTexts.put(ctx, s1+s2);
        }
        else if(startsWithIdent(ctx)) {
            String s1, s2, s3 = "";
            switch(ctx.getChildCount()) {
                case 1:
                    newTexts.put(ctx, ctx.IDENT().getText());
                    break;
                case 3:
                    s1 = ctx.IDENT().getText();
                    s2 = newTexts.get(ctx.expr(0));
                    newTexts.put(ctx, s1+" = "+s2);
                    break;
                case 4:
                    if(ctx.expr().size()>0) {
                        s1 = ctx.IDENT().getText();
                        s2 = newTexts.get(ctx.expr(0));
                        newTexts.put(ctx, s1+"["+s2+"]");
                    }
                    else {
                        s1 = ctx.IDENT().getText();
                        s2 = newTexts.get(ctx.args());
                        newTexts.put(ctx, s1+"("+s2+")");
                    }
                    break;
                case 6:
                    s1 = ctx.IDENT().getText();
                    s2 = newTexts.get(ctx.expr(0));
                    s3 = newTexts.get(ctx.expr(1));
                    newTexts.put(ctx, s1+"["+s2+"]"+" = "+s3);
            }
        }
        else {
            newTexts.put(ctx, ctx.LITERAL().getText());
        }
    }
    @Override
    public void exitArgs(MiniCParser.ArgsContext ctx) {
        if(ctx.getChildCount()>0) {
            List<MiniCParser.ExprContext> exprs = ctx.expr();
            String[] temp = new String[exprs.size()];
            for(int i=0; i<exprs.size(); i++) {
                temp[i] = (exprs.get(i)).getText();
            }
            newTexts.put(ctx, String.join(", ", temp));
        }
        else {
            newTexts.put(ctx, "");
        }
    }
}
