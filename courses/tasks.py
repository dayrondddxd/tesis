# # tasks.py
# from celery import shared_task
# @shared_task
# def sync_course_to_moodle_task(course_id):
#     # ... misma lógica que en la señal
#     @receiver(post_save, sender=Course)
#     def trigger_sync(sender, instance, created, **kwargs):
#         if created:
#             sync_course_to_moodle_task.delay(instance.id)