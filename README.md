

WritersHub.com is an application intended allow users write stories in form 
of blogs for their expression and those of others.

## USER STORIES TARGETED 

View the blog posts on the site
Comment on blog posts
View the most recent posts
Email alert when a new post is made by joining a subscription.
See random quotes on the site
Sign in to the blog.
Create a blog from the application.
Delete comments that are insulting or degrading.
Update or delete blogs created.



## User interface model/design snippet 
[Click here for Design in Figma](https://www.figma.com/file/DufPeR45G6iLdMajXFggHt/WritersHub.Com)

Landing Page
![image description](app/static/land.png)

Blog page
![image description](app/static/blog.png)

Comment Page
![image description](app/static/comment.png)







## Behavior Driven Development 



 <table>
    <thead>
      <tr>
        <th>Behaviour</th>
        <th></th>
        <th>Input</th>
         <th></th>
        <th>keepUpperCase is true</th>
      </tr>
    </thead>
    <tbody>
        <tr>
            <td>1. Application starts</td>
            <td></td>
            <td><code>Application  loads </code></td>
            <td><code></code></td>
            <td>see all available blogs and some inspiring quotes</td>
        </tr>
         <tr>
            <td>2. Login</td>
            <td></td>
            <td><code>Information collected:
            a)user email 
            b) user Password/passcode 
            </code></td>
            <td><code></code></td>
            <td>If account already exists redirect to home page and user can see the blogs and subscribe to get updates</td>
        </tr>
         <tr>
            <td>3. Sign up/ Register</td>
            <td></td>
            <td><code>a) Username, b)user email, and c)user password</code></td>
            <td><code></code></td>
            <td>see all available blogs and some inspiring quotes</td>
        </tr>
    </tbody>
  </table>

The following is a live link to the project:

## Installation process

To access my repository link:

[Click here](https://github.com/Charity-Mutembei/BLOG-APP)

​

*To clone this repository locally, type the following command on your terminal.*

​

If using HTTP keys, type:

​

`https://github.com/Charity-Mutembei/BLOG-APP'


​


​

On running the commands successfully, you should have a local version of this repository.

Navigate to the target directory and open it with a prefered IDE :

1. On running the application, type the following on the terminal;

+ `chmod a+x start.sh`

Then type

`./start.sh`

2. To test the application;

+ `python3.8 manage.py test`

​

3. To navigate to a local browser, Type this on a preferred browser:

+ `127.0.0.1:5000`

## Technologies used

* [Python3.8](https://www.python.org/)

* [Flask](http://flask.pocoo.org/)

* [Heroku](https://heroku.com)

## Known-Bugs

The application is yet to be launched to Heroku.However, the link to the blog is unresponsive, the navbar cannot display the signin and signout option due to constant crashing of the code. 

## Contact information

+ Author E-mail ; `charity.mutembei@student.moringaschool.com`

+ Phone Number: +254 718020830.

## Copyright and License

Copyright (c) 2022 Mutembei Charity

​

`MIT LICENSE`

​

Copyright (c) 2022 

​

Permission is hereby granted, free of charge, to any person obtaining a copy

of this software and associated documentation files (the "Software"), to deal

in the Software without restriction, including without limitation the rights

to use, copy, modify, merge, publish, distribute, sublicense, and/or sell

copies of the Software, and to permit persons to whom the Software is

furnished to do so, subject to the following conditions:

​

The above copyright notice and this permission notice shall be included in all

copies or substantial portions of the Software.

​

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,

OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

SOFTWARE.







