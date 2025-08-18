import os


def main():
    print("Hello, world!")
    try:
        secret_ps = os.environ["MY_PASSWORD"]
        print(
            "You set up your password! Now, remember to not share your secret password in git!"
        )
    except:
        print(
            "You did not set up your password! Please set up your password in the environment variable MY_PASSWORD"
        )


if __name__ == "__main__":
    main()
