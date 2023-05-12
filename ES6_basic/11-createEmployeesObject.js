export default function createEmployeesObject(departmentName, employees) {
    let content = {
        [departmentName]: employees
    };
    return content;
}
