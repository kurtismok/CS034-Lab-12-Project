from set import Set

class EnrollmentManager:
    def __init__(self):
        self.courseA = Set()
        self.courseB = Set()

    def readFile(self, filename, courseSet):
        with open(filename, 'r') as file:
            for line in file:
                student_id = line.strip()
                courseSet.add(student_id)

    def print(self):
        inBoth = self.courseA.intersection(self.courseB)
        onlyA = self.courseA.difference(self.courseB)
        onlyB = self.courseB.difference(self.courseA)
        all_students = self.courseA.union(self.courseB)

        print("Students in both courses:")
        print(inBoth._elements)
        print("\nStudents only in Course A:")
        print(onlyA._elements)
        print("\nStudents only in Course B:")
        print(onlyB._elements)
        print("\nAll students in either course:")
        print(all_students._elements)

if __name__ == "__main__":
    enrolled = EnrollmentManager()
    enrolled.readFile("courseA.csv", enrolled.courseA)
    enrolled.readFile("courseB.csv", enrolled.courseB)
    enrolled.print()
