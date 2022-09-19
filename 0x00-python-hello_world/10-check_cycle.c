#include "lists.h"
/**
 * check_cycle -  check if cycle exists
 * @list: list to be checked
 * Return: 0 if non-existent, 1 if present
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *p = list;

	while (s && p && p->next)
	{
		s = s->next;
		p = p->next->next;
		if (s == p)
			return (1);
	}
	return (0);
}
