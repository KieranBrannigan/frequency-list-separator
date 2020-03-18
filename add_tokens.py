def main():
    s = """
    To quit press ctrl+c at any time or close the window.
    Please place the frequency list in the script's parent directory.
    Make sure it is called 'frequency.json'. 
    It should be a json list of words, nothing else. eg ["的", "我", "你",...] 
    It will be renamed to 'frequency_with_tokens.json'.
    Then type the number for the language of the frequency list and Hit ENTER.
    1. Chinese
    More to come...
    """

    selection = input(s)

    input_file = "frequency.json"

    if selection.lower() == "chinese" or selection.lower() == "1":
        import chinese
        return True

    else:
        print("That didn't work. If you want to quit press CTRL + C")
        return

if __name__ == "__main__":
    a = None
    while not a:
        a = main()
    input("FINISHED. Press ENTER to EXIT.")