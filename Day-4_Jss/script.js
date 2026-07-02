class Student {
  constructor(id, name, marks) {
    this.id = id;
    this.name = name;
    this.marks = marks;
  }
}

let students = [
  new Student(101, "Rahul", 95),
  new Student(102, "Priya", 82),
  new Student(103, "Kiran", 67),
  new Student(104, "Suresh", 45),
  new Student(105, "Anitha", 91),
];

function grade(m) {
  if (m >= 90) return "Grade A";
  if (m >= 75) return "Grade B";
  if (m >= 60) return "Grade C";
  return "Fail";
}

console.log("----- STUDENT REPORT -----\n");

let total = 0,
  pass = 0,
  fail = 0;
let topper = students[0];

for (let s of students) {
  console.log(`ID:${s.id} | ${s.name} | ${s.marks} | ${grade(s.marks)}`);

  total += s.marks;

  if (s.marks >= 60) pass++;
  else fail++;

  if (s.marks > topper.marks) topper = s;
}

console.log("\nTopper: " + topper.name + " (" + topper.marks + ")");

console.log("\nPassed Students:");
for (let s of students) if (s.marks >= 60) console.log(s.name);

console.log("\nFailed Students:");
for (let s of students) if (s.marks < 60) console.log(s.name);

console.log("\nAverage Marks: " + Math.round(total / students.length));
console.log("\nTotal Passed: " + pass);
console.log("Total Failed: " + fail);
