def is_productive(read_pages, free_time):
    # შემოწმება, თუ მინიმუმ 20 გვერდი არის წაკითხული და თავისუფალი დრო არის
    if read_pages >= 20 and free_time:
        return True
    else:
        return False

# ტესტი
read_pages = 25
free_time = True

productive = is_productive(read_pages, free_time)
print(f"Is productive? {productive}")
