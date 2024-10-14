# What is it about : 

This project is for now just a group of page that enable to register in database 
some youtube video links with the title of the video associated with it.

# Future implementation

One of the future go would be to broadcast youtube videos from the back-end, to the computer receiving. The goal would be to play videos just like spotify but by broadcasting youtube content.

# How to start the project :

Choose the "src" folder as the "Sources Root".
Add the dependecies that are in the folder named : 
"dependencies_for_VideoConverter"
to enable to use "SpringBoot".
If it is asked, defined them as "Jar directories".

Go to the pom.xml file, right-click in the file and choose to 
consider this file as maven project.

If you have this error :

```
BeanDefinitionStoreException: Failed to parse
```
Go to maven menu and click on "clean" and the two arrow in circle
"reload all maven incremental".
Now the Application.java should work


In order to run the project, 

1) in a first terminal :
```bash
cd javaForYoutubeDownloader/youtube-converter
/src/main/java.nate.company/
```
run the Application.java file
(you can also run this file from intellij)


3) in a second terminal :
```bash 
cd javaForYoutubeDownloader/youtube-converter
/src/main/java.nate.company/angular/angularclient
```
run the following command : 
```bash
ng serve --open
```






