#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

listint_t *reverse_list(listint_t *head);
int compare_lists(listint_t *list1, listint_t *list2);

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to a pointer to the first node of the list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	listint_t *slow = *head, *fast = *head;
	listint_t *prev_slow = NULL, *mid_node = NULL;
	listint_t *second_half = NULL;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}
	second_half = slow;
	prev_slow->next = NULL;
	second_half = reverse_list(second_half);
	is_palindrome = compare_lists(*head, second_half);
	second_half = reverse_list(second_half);
	if (mid_node != NULL)
	{
		prev_slow->next = mid_node;
		mid_node->next = second_half;
	}
	else
	{
		prev_slow->next = second_half;
	}
	return is_palindrome;
}

/**
 * reverse_list - Reverses a singly linked list.
 * @head: Pointer to the first node of the list.
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next = NULL;
	
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return prev;
}

/**
 * compare_lists - Compares two singly linked lists.
 * @list1: Pointer to the first node of the first list.
 * @list2: Pointer to the first node of the second list.
 * Return: 0 if the lists are not equal, 1 if the lists are equal.
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return 0;
		list1 = list1->next;
		list2 = list2->next;
	}
	if (list1 == NULL && list2 == NULL)
		return 1;
	else
		return 0;
}
