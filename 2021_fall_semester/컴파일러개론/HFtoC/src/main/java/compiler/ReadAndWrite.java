package compiler;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class ReadAndWrite {
    public static void main(String[] args) throws IOException {
        try {
            //테스트 하실때는 아래 경로를 바꿔주시면 되겠습니다
            File sourceFile = new File("/Users/oponeuser7/Desktop/남용우_2021_2학기/컴파일러개론/과제/HFtoC/src/main/java/test.hf");
            File resultFile = new File("/Users/oponeuser7/Desktop/남용우_2021_2학기/컴파일러개론/과제/HFtoC/src/main/java/test.c");
            List<String> list = new ArrayList<>(); //파일 내용을 저장할 리스트
            //파일을 읽고 쓰기 위해 BufferedReader와 BufferedWriter 사용
            BufferedReader bufferedReader = new BufferedReader(new FileReader(sourceFile));
            BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(resultFile));
            String line;
            while((line = bufferedReader.readLine()) != null) {
                list.add(line); //소스 파일을 한 줄씩 읽어서 리스트에 저장
            }
            Analyzer analyzer = new Analyzer();
            List<String> result = analyzer.compile(list); // 이 줄에서 컴파일이 실행됩니다
            for(String temp : result) {
                if(resultFile.isFile() && resultFile.canWrite()){
                    bufferedWriter.write(temp); //컴파일 결과를 한 줄씩 읽어서 파일에 쓴다
                    bufferedWriter.newLine();
                }
            }
            bufferedReader.close();
            bufferedWriter.close();
        } catch(FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}