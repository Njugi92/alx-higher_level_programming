#include <Python.h>

/**
 * print_python_list_info - the function Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, j;
	PyObject *obj;

	size = Py_SIZE(k);
	alloc = ((PyListObject *)k)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (j = 0; j < size; j++)
	{
		printf("Element %d: ", j);

		obj = PyList_GetItem(k, j);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
