# albemic -python 
a intro tutorial to track databse migration scripts



# intro tutorial: 
https://medium.com/@sutharprashant199722/how-to-use-alembic-for-your-database-migrations-d3e93cacf9e8

``` univon app:<func_name>```


# Consumer Profile: Table Creations

Consumer Profile database creation on Aurora DB

1. (Optional) To test it locally, please run mysql on your local machine:

```
docker run --name mysql -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=commonsDB -p 3306:3306 -d mysql:5.7
```

2. Update the changes of the model using:

```
alembic revision --autogenerate -m "<YOUR-MESSAGE>"
```

3. Commit the changes to database:

```
alembic upgrade head
```




# a nice youtube tutorial on starletter- graphql
[2]: [link to youtube tutorial!](https://www.youtube.com/watch?v=-0uxxht4mko&list=PL525MR2zVGh96WZ3YLxcxfVP6OVCb2zhj)

[1]: [I'm an inline-style link](https://www.google.com)


~~the link shoud work by now!~~
Here's our logo (hover to see the title text):

Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

Reference-style: 
![alt text][logo]

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"



[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../blob/master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links. 
http://www.example.com or <http://www.example.com> and sometimes 
example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

[arbitrary case-insensitive reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com
