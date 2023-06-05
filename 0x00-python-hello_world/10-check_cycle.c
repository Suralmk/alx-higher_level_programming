#include "lists.h"
/**
 * check_cycle - checks if there exists a loop or cycle
 * @list: head of the linked list
 * Return: return 1 on success and 0 on fail
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
