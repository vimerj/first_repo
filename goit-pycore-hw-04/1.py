import re


def total_salary(path):
    total = 0
    list_avg = []
    path = "hw04_salary.txt"
    
    with open(path, "r") as file:
        while True:
            line = file.readline()
            salary_avg = re.search(r'\d+', line)

            if salary_avg:
                list_avg.append(int(salary_avg.group()))
            if not line:                
                break
            salary = re.search(r'\d+', line)
            if salary:
                total += int(salary.group())
    
    avg = int(total / len(list_avg))
    salaries_list = [total, avg]
    
    return salaries_list

print(total_salary('salary.txt'))
print(f"Total salary: {total_salary('salary.txt')[0]}, Average salary: {total_salary('salary.txt')[1]}")
