def progress(index, length):
    """
        Prints a progress display bar to the terminal
        Uses c-style techniques,
        ARGS
            index   -> current position in data
            length  -> total length of data
    """
    if index < (length - 1):
        term_width = get_terminal_size()[0] - 20
        chars = (int((index / length * term_width)))
        message = ("Progress: [ " + "\b->" * chars + " " * ((term_width - 1) - chars) + "] "
                   + str(int((chars / (term_width - 1)) * 100)) + "%")
        stdout.write("\r%s" % message)
    else:
        stdout.write("\b\b\b\b\b\b\b-] DONE.\n\n")