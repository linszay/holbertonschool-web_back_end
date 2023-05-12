export default function createEmployeesObject(departmentName, employees) {
  const content = {
    [departmentName]: employees,
  };
  return content;
}
