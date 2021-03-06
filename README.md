<p align="center">
    <img src="doc/logo.svg" height="200px" alt="logo" title="Answerable">
</p>
<h1 align="center">Answerable</h1>
<h3 align="center">Stack Overflow unanswered questions recommendation system</h3>
<p align="center">
	<a href="LICENSE">
        <img alt="license" src="https://img.shields.io/badge/license-MIT-informational">
    </a>
	<img alt="repo-size" src="https://img.shields.io/github/repo-size/MiguelMJ/Answerable">
	<img alt="python3.8" src="https://img.shields.io/badge/python-3.8-informational">  
	<a href="https://github.com/psf/black">
        <img alt="code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
    </a>
</p>

Answerable is a Python program that learns from your answers in Stack Overflow and use them to recommend you questions that you could answer.

___This project is still under development.___ [![last commit](https://img.shields.io/github/last-commit/MiguelMJ/Answerable)](https://github.com/MiguelMJ/Answerable)

**Table of contents**

<span id="toc"></span>

  - [Quick guide](#Quick-guide25)
    - [The .config file](#The-.config-file42)
    - [Where to get the user ID and tags file](#Where-to-get-the-user-ID-and-tags-file46)
  - [Contributors](#Contributors68)
  - [To do](#To-do74)
  - [Contributing](#Contributing91)
  - [License](#License100)

<h2 id="Quick-guide25">Quick guide</h2> 

[[TOC](#toc)]

- **Save your user**

	```
	python answerable.py -s ID [SOURCE-FILE]
	```
	
- **Get recommendations from the latest questions**

	```
	python answerable.py [-u ID [SOURCE-FILE]]
	```


<h3 id="The-.config-file42">The .config file</h3> 

The most probable thing is that you will be using this program with your user, repeteadly. For this reason, instead of having to call Answerable always with the `-u|--user` and `-t|--tags`, you can save them to this file and the following executions will read them from it.

<h3 id="Where-to-get-the-user-ID-and-tags-file46">Where to get the user ID and tags file</h3> 

You can find your id in the url of your profile, that has the following form:

```
https://stackoverflow.com/users/{id}/{name}
```

The tags file requires few extra steps. The reason is that, for now, I won't be implementing the use of the authentication_token for the Stack Exchange API, and to obtain the tags the program must scrap the page. However, this page is private, so you must download. This should be simple. 

1. Go to the following page:

   ```
   view-source:https://stackoverflow.com/users/tag-notifications/{id}
   ```

2. Select all (`Ctrl+A`).

3. Copy and paste in a new file in your system.

   That will be the tags file.

<h2 id="Contributors68">Contributors</h2> 

[[TOC](#toc)]

Be the first on this list!

<h2 id="To-do74">To do</h2> 

[[TOC](#toc)]

- [x] Use `argparse` to interpret the CLI options.
- [ ] ~~Implement all commands.~~
- [ ] Document new behaviour
- [ ] Test and improve the learning models.
- [ ] Complete documentation.
- [ ] Adapt behaviour for users with authentication token.

**Low priority**

- [ ] Include the rest of the Stack Exchange communitites.
- [ ] Make a GUI.
- [ ] Display statistics about the information taken into account to make the recommendations.

<h2 id="Contributing91">Contributing</h2> 

[[TOC](#toc)]

- In addition to the tasks listed above, you can also contribute by testing the program yourself and reporting any bugs in an issue.
- Give this project some visibility:
  - :star: Star this repository ![](https://img.shields.io/github/stars/MiguelMJ/Answerable?style=social).
  - :arrow_up: Upvote it in [Stack Apps](https://stackapps.com/questions/8805/placeholder-answerable-a-recomendator-of-unanswered-questions).

<h2 id="License100">License</h2> 

[[TOC](#toc)]

Answerable uses the MIT license, a copy of which you can find [here](LICENSE), in the repo.

