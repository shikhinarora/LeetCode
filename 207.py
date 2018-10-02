# 207
# https://leetcode.com/problems/course-schedule/description/


class Solution(object):
    """
    :type num_courses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """

    courses = {}

    queue = []
    final_stack = []

    def canFinish(self, num_courses, prerequisites):
        for i in range(num_courses):
            self.courses[i] = []

        for pre in prerequisites:
            if len(pre) > 0:
                course = pre[0]
                dep = pre[1]

                temp = self.courses.get(course, [])
                temp.append(dep)
                self.courses[course] = temp

        for i in range(num_courses):
            if not self.do_dfs_new(i):
                return False

        return True

    def do_dfs_new(self, course):
        if course in self.queue:
            return False

        self.queue.append(course)

        if course in self.final_stack:
            return True
        else:
            deps = self.courses[course]

            for dep in deps:
                if not self.do_dfs_new(dep):
                    return False

            self.queue.remove(course)
            self.final_stack.append(course)
            return True

        return True
