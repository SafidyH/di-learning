class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items or []
        self.pageSize = int(pageSize)
        self.totalPages = 0
        self.currentPage = 1
        self.updateTotalPages()

    def updateTotalPages(self):
        self.totalPages = (len(self.items) - 1) // self.pageSize + 1

    def getVisibleItems(self):
        start = (self.currentPage - 1) * self.pageSize
        end = start + self.pageSize
        return self.items[start:end]

    def prevPage(self):
        self.currentPage = max(self.currentPage - 1, 1)
        return self

    def nextPage(self):
        self.currentPage = min(self.currentPage + 1, self.totalPages)
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        page = int(pageNum)
        if page < 1:
            self.currentPage = 1
        elif page > self.totalPages:
            self.currentPage = self.totalPages
        else:
            self.currentPage = page
        return self

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

p.getVisibleItems()  # ["a", "b", "c", "d"]

p.nextPage()

p.getVisibleItems()  # ["e", "f", "g", "h"]

p.lastPage()

p.getVisibleItems()  # ["y", "z"]

p.goToPage(10)  # p.currentPage will be set to 5 (closest valid page)

p.getVisibleItems()  # Items from the last page (["y", "z"])
