# Welcome

Welcome to CS 24!  This assignment will make sure you have  Git set up correctly
and are ready to submit your programming projects to Gradescope.


## Git Repo Setup

This class  will use a  single Git repo  for the whole quarter.  Each assignment
will get its own folder within  that repo.  You'll create  a private fork of the
main class repo;  I'll push code to the class repo  as assignments are released,
and you can pull to get the code.

Normally you'd  fork the class repo on GitHub,  but GitHub doesn't allow private
forks of public repos, so this'll be a little more complicated.

First, set up your GitHub account and create a new empty repo:

- Create a GitHub account if you don't already have one.
- Add your SSH key to your GitHub account if it's not there already:
  - Check to see if you have an [existing SSH key][ssh-exists] on your computer.
  - If you don't already have an SSH key, [create one][ssh-create].
  - [Add your SSH key][ssh-github] to your GitHub account.
- Create a new repo on GitHub.
  - Don't initialize it with any files.
  - Make sure it's private.

Then download the class repo onto your local machine and configure it to talk to
both GitHub repos:

- [Install and configure Git][git-setup] if you don't have it already.
- Clone the class repo somewhere on your local machine.
- The class repo will be at a remote named `origin`; rename it to `upstream`.
- Add a new remote for your GitHub repo; call it `origin`.  Use the SSH URL.
- Push your local `master` branch to your GitHub repo (and set it as your
  default push target with the `-u` option):
  ```sh
  git push -u origin master
  ```
- Your files should now be visible in the GitHub web UI.

Then check that you have everything set up correctly:

- Make sure the output of `git remote -v` makes sense.
- Save the output of `git remote -v` as `welcome/remotes.txt`.
- Commit this file and push it to your GitHub repo.


## Git Branches

Now that your repo is set up, get some practice merging:

- The class repo contains three extra branches:
  - `fishwife`
  - `jabberwocky`
  - `shi`
- Merge all of these into your `master` branch.
- Push your changes to your GitHub repo.


## Some Code

Then write some code.

- Create the folder `welcome/code`.
- Create an `olleh.cpp` file in that folder. It should compile to a program that
  reads a single  line from the console,  then prints that line with the letters
  of each word reversed.  Words are separated by whitespace and/or punctuation:
  ```
  [user@host code]$ ./olleh
  It cost $349.95, but I bought it anyway.
  tI tsoc $943.59, tub I thguob ti yawyna.
  [user@host code]$ 
  ```
- Create a `Makefile` inside your `welcome/code` folder.
  - Running `make` in that folder should compile `olleh.cpp` to `olleh`.
  - Running `make clean` in that folder should the executable and any object files.
  - Running `make clean` should succeed even if there is no executable.


## Commit and Submit

- Commit all your changes and push them to GitHub.
- Submit your GitHub repo to Gradescope.
  - You'll be asked to connect your GitHub account to Gradescope if you haven't already.
- Make sure all the tests pass.


## Git Hints

- A Git cheatsheet that may prove helpful:\
  https://xavierholt.github.io/cheatsheets/git.html
- It's always a good idea to run `git status` and see what state your repo is in.
- Git will open a text editor when you make a merge commit, just in case you
  want to edit the automatically generated commit message.  This will probably
  be Vim, so type `:wq` and hit Enter to accept the message and continue.
- If you use the `-u` (aka `--set-upstream`) option when pushing to your GitHub
  repo, Git will link your local branch with that remote branch, and a simple
  `git push` will push that branch to the correct place in the future.


## Code Hints

- Whitespace and punctuation are defined as in the [cctype][cctype] header.
- Everything that isn't whitespace or punctuation is considered to be a "word" character.
- Your code should always print exactly one newline, regardless of the input.
- Your code must compile with no warnings (see the syllabus).
- Don't check executables or object files into Git.


[github]: https://github.com
[git-setup]: https://help.github.com/en/github/getting-started-with-github/set-up-git
[ssh-exists]: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys
[ssh-create]: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
[ssh-github]: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
[cctype]: https://cplusplus.com/reference/cctype/
