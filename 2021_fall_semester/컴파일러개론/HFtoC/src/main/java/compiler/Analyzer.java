package compiler;

import java.util.ArrayList;
import java.util.List;

class Analyzer {
    /* Analyzer.compile 메소드에서 사용하는 메소드입니다. 괄호를 없앤 HF 소스 코드를 한 줄 받아서 공백을 기준으로 파싱합니다.
    그리고 파싱된 첫 번째 문자열을 보고 어떤 명령인지 알아냅니다. 그 다음에는 HF 코드의 아규먼트 부분을 분리해서
    Generator 클래스의 해당하는 메소드를 사용하여 알맞는 C 코드를 얻어낸 후 리턴합니다.
    모든 아규먼트를 넘길 때에는 헷갈리지 않기 위해서 String.substring 을 이용해 쌍따옴표를 제거합니다.
     */
    String choose(String line) {
        Generator generator = new Generator();
        String[] parsed = line.split(" ");
        switch (parsed[0]) {
            case "start":
                return generator.start();
            case "end":
                return generator.end();
            case "echo":
                return generator.echo(line.substring(6, line.length() - 1));
            case "del":
                return generator.del(line.substring(5, line.length() - 1));
            case "list_dir":
                return generator.listDir();
            case "show":
                return generator.show(line.substring(6, line.length() - 1));
            /*
            mov 는 명령 안에 명령이 있는 형태이기 때문에 취급이 다릅니다. 우선 mov 명령에서 수행 결과를 저장할 파일은
            HF 코드의 맨 마지막 순서로 오기 때문에 공백 기준으로 파싱했을 때 마지막 조각을 가져오면 됩니다. 그 다음 온전한 HF 코드에서
            앞의 mov 부분과 뒤의 수행 결과를 저장할 파일 부분을 제거하면 두 번째 명령을 얻을 수 있습니다. 두 번째 명령의 C 코드 해석과
            수행 결과를 저장할 파일을 아규먼트로 해서 Generator.mov 메소드를 호출합니다.
             */
            case "mov":
                String temp = parsed[parsed.length - 1];
                String target = temp.substring(1, temp.length() - 1); //수행 결과 저장 파일 부분을 분리
                temp = line.substring(4); //mov 부분 제거
                // 추가적으로 -3을 하는 이유는 쌍따옴표(-2)와 공백(-1) 때문입니다.
                String secondLine = temp.substring(0, temp.length() - target.length() - 3);
                return generator.mov(choose(secondLine), target);
            default:
                // 입력에 오류가 있었을 시
                return "Unknown code";
        }
    }
    /*
    유일하게 메인 메소드에서 직접 사용하는 함수입니다. HF 소스 파일을 문자열 리스트에 한 줄씩 담은 것을 아규먼트로 받습니다.
    리턴은 번역이 완료된 문자열 리스트입니다. Analyzer.choose 메소를 사용해 HF 소스 코드를 한 줄씩 번역한 다음 리스트에 담아서
    리턴합니다.
     */
    List<String> compile(List<String> list) {
        List<String> result = new ArrayList<>();
        result.add(choose("start")); // 템플릿 코드 ( import, int main() 등등)
        for (String line : list) {
            // HF의 괄호를 없애기 위해서 String.substring 을 사용해 앞과 뒤에서 캐릭터 하나씩 자릅니다.
            result.add(choose(line.substring(1, line.length() - 1)));
        }
        result.add(choose("end")); // 템플릿 코드 (닫는 중괄호)
        return result;
    }
}
