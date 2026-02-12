"""
CP1404 Practical
"""
import wikipedia


def main():
    """Main function to search and display Wikipedia pages."""
    title = input("Enter page title: ")

    while title != "":

        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
            print()

        except wikipedia.DisambiguationError as e:
            print(f"We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
            print()

        except wikipedia.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
            print()

        title = input("Enter page title: ")

    print("Thank you.")

if __name__ == '__main__':
    main()