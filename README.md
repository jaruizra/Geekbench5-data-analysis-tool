# Geekbench5-data-analysis-tool
This program is a python script that given a valid geekbench 5 test URL it will download the code and analyze the data that appears in the test.

For it to work just download python3 on your computer and double click the geekbench5.py program.

I have created a python script that can get more info out of a given geekbench5 test compared to the official geekbench5 page. For some reason, the official page doesn’t
show the test frequencies and that really bothered me because the data was in the test files, and accessing that test file every time was time consuming, so I made a
python script that makes it easy for everyone.

It works by when given the url sending a request of the data of that test to the geekbench5 page, then it analyze that data and shows you the results.

You can press ctr+c to get out of the script at any given time, and there are menus that tell you what options you have.

After giving the first url, the program will ask you if you want to give another url for comparison or if you just want to analyze that given test. In that case just 
type 1 and it will show you the data.

The test1 will be your first given url and the test2 will be the second given url. 

The program itself is very basic but I will work for making it better in the future. Some ideas are to:
  1. Save the raw data to a .json file.
  2. Save the analyze data to a .json file.
  3. Save the analyze data as a chart in file.
  
If you have some ideas or ways to improve it, please tell me, this is my first program from college and I am still learning, still the program was done in a hurry, 
it will improve, and feedback is appreciated. Thanks :).
