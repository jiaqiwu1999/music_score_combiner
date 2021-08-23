# music_score_combiner
A small python program that scrapes a known website's png images and combine them into pdf. Utilizes PIL and PyPDF library.
This programs only works for websites that provide public and login-free access to music scores that's shared by willing individuals

## **Beautiful Soup to find image tags whose "alt" attribute indicates that it's score-related**
![image](https://user-images.githubusercontent.com/59846636/130361296-ae3d867a-aeff-4a3b-9c86-176fdc98a601.png)

## **Download the png files one by one**
The images are saved into before_process file, notice that the png requires us to add an additional white background
A script using wget is also included as an alternative
![image](https://user-images.githubusercontent.com/59846636/130361381-4f1968bb-692f-4d29-8b8a-bed1d442e882.png)

## **Adding background to png using PIL lib**
The processed images are saved in after_process file for bette readability
![image](https://user-images.githubusercontent.com/59846636/130361413-db8956af-a4a3-4d71-b76a-ba4211766a83.png)

## **Combining them into pdf file using PIL and PyPDF lib**
It was noted that PIL's function for saving multiple files did not work locally, so resorting to other library is necessary
