import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.ParseTree;
import gen.*;

public class TestMiniC {
    public static void main(String[] args) throws Exception {
        MiniCLexer lexer = new MiniCLexer(new ANTLRFileStream("./test.c"));
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        MiniCParser parser = new MiniCParser(tokens);
        ParseTree tree = parser.program();
    }
}
