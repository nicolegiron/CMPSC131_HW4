# Author: Nicole Giron nqg5259@psu.edu
def getGradePoint(letter):
  """
  Given a letter grade, translate it into a gradepoint value between 0.0 and 4.0
  YOU MUST USE if/elif/../else structure to implement this function.
  YOU CAN NOT use any features/data structure we haven't learned in the class,
  including but not limited to list, dictionary and tuples.
  """
  if letter == "A":
    return 4.0
  elif letter == "A-":
    return 3.67
  elif letter == "B+":
    return 3.33
  elif letter == "B":
    return 3.0
  elif letter == "B-":
    return 2.67
  elif letter == "C+":
    return 2.33
  elif letter == "C":
    return 2.0
  elif letter == "D":
    return 1.0
  else :
    return 0.0
  return 0.0

def run():
  """
  Use either a while-loop or a for-loop to make your code for getting three separate
  courses' letter grade and credit info. And calculate the final GPA.
  YOU CAN NOT use any features/data structures we haven't learned in the class,
  including but not limited to list, dictionary, and tuples.
  """
  grades = 0
  credits = 0
  for i in range(1, 4):
    grade = getGradePoint(input(f"Enter your course {i} letter grade: "))
    credit = float(input(f"Enter your course {i} credit: "))
    print(f"Grade point for course {i} is: {grade}")
    grades += (grade*credit)
    credits += credit
  
  GPA = grades / credits
  print("Your GPA is: " + str(GPA))
  return

if __name__ == "__main__":
  run()
