import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.ParseTreeWalker;
import gen.*;

public class Main {
    public static void main(String[] args) throws Exception {
        MiniCLexer lexer = new MiniCLexer(new ANTLRFileStream("./src/test.c"));
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        MiniCParser parser = new MiniCParser(tokens);
        ParseTree tree = parser.program();
        ParseTreeWalker walker = new ParseTreeWalker();
        walker.walk(new MiniCPrintListener(), tree);
    }
}