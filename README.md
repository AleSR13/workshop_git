# Git workshop

## Configuration

### View config

```
git config --list
```

### Set config

```
git config --global user.name "Alejandra H Segura"
git config --global user.email "43819685+AleSR13@users.noreply.github.com"
git config --global init.defaultBranch main
```

The branch name "main" is currently more accepted than the name "master" that was used previously.

## Git basics

When you want to modify a repo that exists in GitHub/Gitlab:

```
git clone https://github.com/AleSR13/workshop_git.git
```

When you want to start a repo locally:

```
# Commented out because we are not using it in this workshop
# git init
```

## Git branching

### Create and check out branches

It is always a good idea to have a branch called "dev" (and maybe another one called "stage" or "test" or similar) and not working directly in "main". Like this, you can leave "main" as a working repo whereas "dev" and "test" can be a playground and a space for testing new features, respectively.

Sometimes we want to create new branches that do not exist in our local repo and neither in the remote one (the GitHub website). Keep in mind that the remote repo and your local one are not in sync unless you enforce the synching.

To know which branches you have locally, you can run the command:

```
git branch
```

It will show a list of available local branches and the one in which you are currently located will be highlighted and have a little asterisk (\* symbol) on the left.

Now, to move to the branch "dev", for example, you can do different things based on your status:

1. If the dev branch already exists locally, you can just check it out:

```
git checkout dev
```

To make sure everything is up to date with respect to the remote you can do:

```
git pull origin dev
```

2. If the dev branch exists in GitHub website but you don't have it locally, do:

```
git fetch --all # To fetch all the info of remote branches that you don't have downloaded in your repo
git switch dev # To checkout a branch that so far was only available remotely
```

Now that you are in the dev branch, you may want to add a new feature or change to your original code. You don't do it directly in dev. Instead, you create a new branch off dev. So, dev will be the base you will use to create the changes.

```
git checkout -b feat/ale_greeting
```

With this, I create a feature branch specifically for my feature "Ale greeting". In the next steps we will change the code in there.

### Add changes to your branch

Make changes. For example, add a file in the root directory called `.env` and add the content:

```
MY_PASSWORD="super_secret_password"
```

Once you make changes to some of the files you can "stage" them. Before the staging you can perform a dry run to see what will be staged:

```
git add . -n
```

Add first a `.gitignore` file in the root directory and enlist stuff you don't want to end up in your git repo:

```
.env
```

Now you see that only the `.gitignore` appears as "to be staged" because you haven't changed anything else except an ignored file. Now we can change a real file!

Go to the file `src\hello_world.py` and see what it does. You can test it running the following command in Windows:

```
python .\src\hello_world.py
```

In Linux or MacOS the command would be:

```
python src/hello_world.py
```

Now, change something in the `src\hello_world.py` file. For example, in line 5, instead of "Hello, world!" it should greet with "Hello, <your name>!"

Now, you can stage it, commit it and push it to your branch!

```
git add . -n
# Review changes
git add .
git commit -m "[FEAT] Specific greeting for Ale"
git push origin feat/ale_greeting
```

The new branch will be created also in the remote GitHub!

### Pull request and merge (within GitHub)

This is a bit advanced and you need to do it together with the instructor. Here I only give the steps but the instructor can show you in the UI how it works:

1. Create a pull request with a good name and description
2. Add a reviewer to your branch (another team member or the instructor)
3. The reviewer should do a code review commenting on your code and approving or requesting changes
4. If you get a request for changes, you can address them (modify your code accordingly), answer to the comments in the code review and close the threads. The let the reviewer know so he/she/they can review again
5. Once approved, merge the pull request (one at a time for every participant)
6. If a merge conflict emerges (and if everyone follow instructions, it will!), solve it either in the UI or in your laptop
7. Usually, after merge, you will check that everything works fine in the dev code (integration test)
8. Some teams have an extra check in a new branch called test or stage. This branch is creating by making a pull request from the dev branch to the test branch. There they check once more everything works
9. Finally, if everything works, they do a merge request from test to main and create a tag and a release

Some of this is very advanced. In small projects, you may not use more than main, dev and feature branches. I recommend to leave the training until step 6 or 7 as an intro and go further only if the project or team may need it.

## Tag and release

Once you are happy with your code in the main branch, you can create a "tag" and even a "release". Tags are a way to mark certain commits as being of special importance. The release is a way to bundle your code in a specific commit/tag so that it is easier to browse and download. The tags are part of git functionality, but the releases are something more specific to the platform where you run git (e.g. GitHub or Gitlab).

To enlist existing tags do:

```
git tag
```

To create a tag do:

```
git tag -a "v1.0.0" -m "Version 1 contains code for saying hello to the world through python"
```

Note that there cannot be duplicated tags. That is why tags usually have certain conventions with a notation like the one I used (`v.0.1.0`) where the `v`means `version`; the first number is the "major release" indicating major changes in the code and likely lack of compatibility between major versions; the second number means "minor release" indicating extra features with respect to the previous release; finally, the last number refers to a "patch", which basically means a small bug fix or some update for security that does not affect functionality.

Tags are nice because afterwards, you can use them to "move into them" to do rollbacks or to make branches off them. I won't explain how that works here but know it is possible!

By default, `git push` does not transfer tags to remote server. You have to explicitly push tags like this:

```
git push origin --tags
```

Now, to create a release in GitHub, you have to do it through the UI. There, you can go to the menu for releases (right side of the main page of your repo) and create a new release. It will ask you to choose one of the tags you gave. You can select it and give some description before releasing.

That was it! Success using git!
