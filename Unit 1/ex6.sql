CREATE OR REPLACE PROCEDURE dept_statistics (
    p_deptno     IN  NUMBER,
    p_total_emp  OUT NUMBER,
    p_avg_sal    OUT NUMBER,
    p_max_sal    OUT NUMBER
)
IS
BEGIN
    SELECT COUNT(*),
           AVG(sal),
           MAX(sal)
    INTO p_total_emp,
         p_avg_sal,
         p_max_sal
    FROM emp
    WHERE deptno = p_deptno;
END;
/
DECLARE
    v_total_emp NUMBER;
    v_avg_sal   NUMBER;
    v_max_sal   NUMBER;
BEGIN
    dept_statistics(
        10,
        v_total_emp,
        v_avg_sal,
        v_max_sal
    );

    DBMS_OUTPUT.PUT_LINE('Total Employees : ' || v_total_emp);
    DBMS_OUTPUT.PUT_LINE('Average Salary  : ' || v_avg_sal);
    DBMS_OUTPUT.PUT_LINE('Maximum Salary  : ' || v_max_sal);
END;
/

