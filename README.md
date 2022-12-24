# Geekbench5-data-analysis-tool
This program is a python script that given a valid geekbench 5 test URL it will download the code and analyze the data that appears in the test.

I have created a python script that can get more info out of a given geekbench5 test compared to the official geekbench5 page. For some reason, the official page doesn’t show the test frequencies and that really bothered me because the data was in the test files, and accessing that test file every time was time consuming, so I made a python script that makes it easy for everyone.

![Captura de pantalla 2022-12-24 121702](https://user-images.githubusercontent.com/121313957/209433446-e25dd0d6-a9ad-44c7-872b-5b5abdb75c49.png)

# Install python
In this link you can find the official beginner guide to installing python, it is really easy:

     https://wiki.python.org/moin/BeginnersGuide/Download

For it to work just download python3 on your computer and double click the geekbench5.py program.

# Usage
You will need to import some python modules, for that you will need to type on your pc terminal after installing python:

     pip3 install Beautifulsoup
     pip3 install requests
     pip3 install requests.exceptions
     pip3 install json

(If pip3 doesnt work try doing the same but with pip, it will depend of the version of python that you use.)


The program works by when given the url sending a request of the data of that test to the geekbench5 page, then it analyze that data and shows you the results.
Just copy the link to a given test url like this one:

![Captura de pantalla_20221223_210838](https://user-images.githubusercontent.com/121313957/209401492-d6a0abc1-4683-4648-8e2e-2fcd02175e95.png)

You can press ctr+c to get out of the script at any given time, and there are menus that tell you what options you have.

After giving the first url, the program will ask you if you want to give another url for comparison or if you just want to analyze that given test. In that case just 
type 1 and it will show you the data:

![Captura de pantalla 2022-12-24 121702](https://user-images.githubusercontent.com/121313957/209433456-9f9e0428-8b1b-4c0e-b49d-7ef29556a122.png)

In case you add a second url, test1 will be your first given url and the test2 will be the second given url:

![Captura de pantalla 2022-12-24 121718](https://user-images.githubusercontent.com/121313957/209433485-e8123bb7-4c56-479f-a605-da4c657b36f6.png)

# Disclaimer

It has been primarly design and tested with android phones in mind, it will certain show you good info. If you try to use it for another test of another platform it may show incorrect data in the final page, so take that into consideration when using it

# Future

The program itself is very basic but I will work for making it better in the future. Some ideas are to:
  1. Save the raw data to a .json file.
  2. Save the analyze data to a .json file.
  3. Save the analyze data as a chart in file.
  
If you have some ideas or ways to improve it, please tell me, this is my first program from college and I am still learning, still the program was done in a hurry, 
it will improve, and feedback is appreciated. Thanks :).
