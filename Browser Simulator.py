class BrowserSimulator:
    def __init__(self):
        self.history = []
        self.current_index = -1

    def visit_page(self, page):
        if self.current_index != len(self.history) - 1:
            self.history = self.history[: self.current_index + 1]
        self.history.append(page)
        self.current_index += 1

    def back(self):
        if self.current_index > 0:
            self.current_index -= 1
            return self.history[self.current_index]
        else:
            print("Can't go back further.")
            return None

    def forward(self):
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
            return self.history[self.current_index]
        else:
            print("Can't go forward further.")
            return None

    def current_page(self):
        return self.history[self.current_index] if self.current_index >= 0 else None

# Example Usage:
browser = BrowserSimulator()
browser.visit_page("Homepage")
browser.visit_page("About Us")
browser.visit_page("Contact")
print("Current Page:", browser.current_page())
print("Back:", browser.back())
print("Current Page:", browser.current_page())
print("Forward:", browser.forward())
print("Current Page:", browser.current_page())
