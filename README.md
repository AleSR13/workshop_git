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

Create branches in your repo (if not existing):

```
# May fail if it already exists
git checkout -b dev
```

It is always a good idea to have a branch called "dev" (and maybe another one called "stage" or "test" or similar) and not working directly in "main". Like this, you can leave "main" as a working repo whereas "dev" and "test" can be a playground and a space for testing new features, respectively.

If the dev branch already exists, you can just check it out

```
git checkout dev
```

We all create one branch with our name:

```
git checkout -b feat/ale
```

### Add changes to your branch

Make changes. For example, add a file in the root directory called `.env.ps1` and add the content:

```
$env:MY_PASSWORD="super_secret_password"
```

Once you make changes to some of the files you can "stage" them. Before the staging you can perform a dry run to see what will be staged:

```
git add . -n
```

Add first a `.gitignore` file in the root directory and enlist stuff you don't want to end up in your git repo:

```
.env.ps1
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
git push origin feat/ale
```

The new branch will be created also in GitHub!

### Within GitHub

This is a bit advanced, so we can do it together

1. Create a pull request with a good name and description
2. Merge the pull request (one at a time)
3. If a merge conflict emerges (and if everyone follow instructions, it will!), solve it either in the UI or in your laptop

## Get all updates from your branch

```
git checkout dev
git pull origin dev
```
