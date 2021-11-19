package compiler;

/*
목적 코드(C 코드)를 생성하는 클래스입니다. 모든 C 코드들은 system 함수를 사용합니다. mov 명령을 사용하면 수행 결과를
파일에 저장해야 하는데 system 함수에서 '명령어 > 파일명' 옵션을 통해 편리하게 구현할 수 있기 때문입니다.
 */
class Generator {
    String start() {
        return "#include <stdio.h>\n#include <stdlib.h>\nint main() {"; //템플릿 코드
    }
    String end() {
        return "}"; //템플릿 코드
    }
    String echo(String line) {
        return "system(\"echo '" + line + "'\");"; //큰따옴표 중복을 피하기 위해 echo 안에 작은따옴표 사용
    }
    String del(String line) {
        return "system(\"rm " + line + "\");";
    }
    String listDir() {
        return "system(\"ls -al\");";
    }
    String show(String line) {
        return "system(\"cat " + line + "\");";
    }
    /*
    mov 함수입니다. 수행할 명령(line)과 출력 결과를 저장할 파일(target)을 파라미터로 가집니다.
     */
    String mov(String line, String target) {
        //line 에서 세미콜론(-1), 닫는 괄호(-1), 큰따옴표(-1)을 제거
        String result = line.substring(0,line.length()-3);
        return result + " > " + target + "\");";
    }
}
