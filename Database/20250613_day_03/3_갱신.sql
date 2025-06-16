/*
5. **`PM` 직책을 가진 모든 직원의 연봉을 10% 인상한 후 그 결과를 확인하세요.**
*/
CREATE INDEX idx_position ON employees(position);
UPDATE employees SET salary = salary * 1.1 WHERE position = 'PM';
SELECT * FROM employees WHERE position = 'PM';

/*
6. **모든 `Backend`' 직책을 가진 직원의 연봉을 5% 인상하세요.**
*/
UPDATE employees 
SET salary = salary * 1.05
WHERE position = 'Backend';