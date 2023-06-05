#include "lists.h"

/**
 * check_cycle - checks for loop or cycle
 * @list: head of linked list
 * Return: 1 if there is cycle and 0 if not
 */

int check_cycle(listint_t *list)
{
listint_t *first, *second;

if (list == NULL)
{
return (0);
}
first = list;
second = list->next;
for (; second && first && second->next;)
{
if (first == second)
{
return (1);
}
first = first->next;
second = second->next->next;
}
return (0);
}
