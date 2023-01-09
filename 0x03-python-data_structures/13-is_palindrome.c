#include "lists.h"

/**
* reverse_listint - reverses a linked list
* @head: pointer to the first node in the list
*
* Return: pointer to the first node in the new list
*/
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
* is_palindrome - checks if a linked list is a palindrome
* @head: double pointer to the linked list
*
* Return: 1 if it is, 0 if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *uno = *head, *dos = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		dos = dos->next->next;
		if (!dos)
		{
			dup = uno->next;
			break;
		}
		if (!dos->next)
		{
			dup = uno->next->next;
			break;
		}
		uno = uno->next;
	}

	reverse_listint(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
