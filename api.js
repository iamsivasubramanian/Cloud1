const express = require('express');
const app = express();
app.use(express.json());
let employees = [
  { id: 152, name: 'Siva', department: 'HR', salary: 50000 },
  { id: 161, name: 'Subu', department: 'Finance', salary: 60000 },
  { id: 90, name: 'Mani', department: 'IT', salary: 70000 }
];
app.get('/', (req, res) => {
  res.send('Welcome to the Employee Management System!');
});
app.get('/employees', (req, res) => res.send(employees));
app.get('/employees/:id', (req, res) => {
  const emp = employees.find(e => e.id === +req.params.id);
  emp ? res.send(emp) : res.status(404).send('Employee not found');
});
app.post('/employees', (req, res) => {
  const emp = req.body;
  if (!emp.id || !emp.name || !emp.department || !emp.salary)
    return res.status(400).send('All fields are required');
  employees.push(emp);
  res.send(emp);
});
app.put('/employees/:id', (req, res) => {
  const emp = employees.find(e => e.id === +req.params.id);
  if (!emp) return res.status(404).send('Employee not found');
  const { name, department, salary } = req.body;
  emp.name = name || emp.name;
  emp.department = department || emp.department;
  emp.salary = salary || emp.salary;
  res.send(emp);
});
app.delete('/employees/:id', (req, res) => {
  employees = employees.filter(e => e.id !== +req.params.id);
  res.send('Employee deleted successfully');
});
const port = 5000;
app.listen(port, () => console.log(`Server running on port ${port}`));
