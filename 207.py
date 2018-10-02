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
            if i not in self.final_stack:
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

    def canFinishOld(self, num_courses, prerequisites):
        """
        :type num_courses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        for _ in range(num_courses):
            self.courses[_] = Course(_, State.idle)

        for _ in prerequisites:
            course_id = _[0]
            dependency_id = _[1]

            self.courses[course_id].add_dependency(dependency_id)

        for _ in self.courses.keys():
            course = self.courses[_]

            if course.get_state() is State.idle:
                course.set_state(State.wip)
                dependencies = course.get_all_dependency()

                for dep in dependencies:
                    if not self.do_dfs(self.courses[dep]):
                        return False

                course.set_state(State.complete)

        return True

    def do_dfs(self, course):
        if course.get_state is State.wip:
            return False

        dependencies = course.get_all_dependency()

        for _ in dependencies:
            dep = self.courses[_]
            dep.set_state(State.wip)
            if not self.do_dfs(dep):
                return False
            else:
                dep.set_state(State.complete)
                return True


class State:
    idle = 1
    wip = 2
    complete = 3


class Course:
    dependency = []

    def __init__(self, course_id, state):
        self.id = course_id
        self.state = state

    def add_dependency(self, course):
        self.dependency.append(course)

    def get_all_dependency(self):
        return self.dependency

    def remove_dependency(self, course):
        self.dependency.remove(course)

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state


print Solution().canFinish(2, [[1, 0], [0, 1]])
