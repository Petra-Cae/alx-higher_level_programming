#include <stdio.h>
#include <Python.h>

/**
* print_python_list_info - prints info about a python list
* @p: pointer to a PyObject
*
*Return: void
*/
void print_python_list_info(PyObject *p)
{
    long int size, a;
    PyListObject *list;
    PyObject *item;

    size = Py_SIZE(p);
    printf("[*] Size of the Python List = %ld\n", size);

    list = (PyListObject *)p;
    printf("[*] Allocated = %ld\n", list->allocated);

    for (a = 0; a < size; a++)
    {
        item = PyList_GetItem(p, a);
        printf("Element %ld: %s\n", a, Py_TYPE(item)->tp_name);
    }
}
