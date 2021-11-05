# <mark style="background-color: white; color: black;"><b>Assess ENIGMA</b></mark>

>Don't judge the name, it's given by me and that's how I am !!

## <mark style="background-color: white; color: black;"><b>Video Discription:</b></mark>  <https://youtu.be/vZalumjvILg>

## <mark style="background-color: white; color: black;"><b>Text Description:</b></mark>

In this project I have tried to develop a web application, in which you can create forums and submit/attempt forums, this web application has its own database where all the data related to usages and creations is stored.<br>
This web application has two interfaces:<br>
- CREATOR
- USER

<br>

<p style="text-decoration:underline"><b>CREATOR:</b></p>In the creator interface, you can create forums that would be submitted/attempted by others. But you have to first register or log in as a creator on the website. <br>After this, you can create forums simply by referring to the 'Create' button on the website. You have to first set the name and password for the forum you are going to create, so that you can give that ID and password to users to submit/attempt that particular forum. After setting all this up, the website will redirect you to a page on which you have the option to add objective and subjective questions according to your need. You can add as many as questions you want, just type the question/options and click add button. To commit and create the forum finally click on the button at the bottom, which says 'Submit and Create'.<br>Now the website will redirect you to a webpage that will show you the forum you created or a list of all the previously created forums. There you also get options like 'Edit and view' and 'Delete'. 'Edit and view' as the name says, by this you can edit and view the forums you created. And by the 'Delete' option you can delete a forum in just one click.<br>When you open 'Edit and view' it shows you all the questions you have added and an option with each question to edit or delete the question. It's very easy to edit a question, just select the part of the question (question or options) you want to edit, type the changes and submit the changes, it will automatically commit all changes in one click. There is one more option on the top of the webpage, that says 'Add question' by which you can add questions to the forum. But that questions will not be added to the same forum, it created a new forum that contains both previously added and newly added questions.
On top, you also get one more option that is 'Responses', in which you can select the forum and see who has submitted/attempted the forum. You can also see their responses by further selection.
<br><br>Now you are all set to distribute your forum ID and password to users, who would attempt/submit the forum you have created.
<br>
<br>
<br>
<p style="text-decoration:underline"><b>USER:</b><p>
In the user interface, you have to just register or log in as a user on this web application. There you will get only two options 'Attempt' and 'Responses'.<br>Here if you want to attempt any forum created by a creator, you have to simply click on attempt and it will request you to enter ID and password, which you will get from the creator and you would be able to add responses to that particular forum. You can also see your responses by clicking on the option on top of the webpage that says 'Responses'. It contains the list of all the forums you have attempted/submitted in past or you are going to attempt/submit in the future.

<br>

## <mark style="background-color: white; color: black;"><strong>Table Of Contents</strong></mark>

- [Application.py](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/application.py)
- [Helpers.py](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/helpers.py)
- [Project.db (Database)](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/project.db)
- [Templates (Contains all .html files)](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/tree/master/templates)
  * [Apology.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/apology.html)
  * [Attempt.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/attempt.html)
  * [Attempting.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/attempting.html)
  * [Create.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/create.html)
  * [Created.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/created.html)
  * [Creates.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/creates.html)
  * [EditO.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/editO.html)
  * [EditS.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/editS.html)
  * [Indexc.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/indexc.html)
  * [Indexu.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/indexu.html)
  * [Layout.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/layout.html)
  * [Login.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/login.html)
  * [Open.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/open.html)
  * [Register.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/register.html)
  * [Responses.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/responses.html)
  * [ResponsesU.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/responsesU.html)
  * [Search.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/search.html)
  * [Submitted.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/submitted.html)
  * [ViewC.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/viewC.html)
  * [ViewU.html](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/templates/viewU.html)
- [Static (Contains all attachments)](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/tree/master/static)
  * [Styles.css](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/static/styles.css)
  * [Background.jpg](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/static/background.jpg)
  * [Books.1.ico](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/static/books.1.ico)
  * [Books.png](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/static/books.png)
  * [error.jpg](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/static/error.jpg)
- [Libraries required to run this web application](https://github.com/Sandhu-Sahil/Assess_ENIGMA_......_Harvard_University/blob/master/requirements.txt)

<br>

<p style="text-decoration: underline overline"><b>TO USE THIS WEB APPLICATION YOU HAVE TO JUST INSTALL AND RUN THIS APPLICATION USING FLASK
<br>AND THEN JUST DISTRIBUTE THE LINK YOU GET FROM FLASK SERVER TO ALL WHO WANT TO USE THIS WEB APPLICATION

<br>

>> A quick word on [Academic Honesty](https://cs50.harvard.edu/x/2021/honesty/). Before copying you should be aware that this web application is under [my](https://github.com/Sandhu-Sahil) copyright, so you can only use this application, can't submit or sanction it under your name. If caught the consequences will be disastrous. So be careful !!
