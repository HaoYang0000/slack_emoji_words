class Character:
    emoji = None
    formatted_string = ''
    SPACE_NUM = 6

    def __init__(self, emoji: str):
        self.emoji = emoji

    def print(self) -> str:
        """
        Using positional and key argument to format each word.
        position 0 is space.
        position 1 is emoji
        line_break is \n

        :return: str
        """
        return self.formatted_string.format(':white_large_square:', self.emoji, line_break="\n")


class A(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{0}{0}{0}{0}{0}{0}{0}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}" \
                                "{0}{0}{1}{0}{1}{0}{0}{line_break}" \
                                "{0}{1}{1}{1}{1}{1}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{1}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{1}{line_break}"


class B(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{1}{1}{1}{1}{0}{0}{0}{line_break}" \
                                "{1}{0}{0}{0}{1}{0}{0}{line_break}" \
                                "{1}{0}{0}{0}{1}{0}{0}{line_break}" \
                                "{1}{1}{1}{1}{1}{0}{0}{line_break}" \
                                "{1}{0}{0}{0}{1}{0}{0}{line_break}" \
                                "{1}{0}{0}{0}{1}{0}{0}{line_break}" \
                                "{1}{1}{1}{1}{0}{0}{0}{line_break}"


class C(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{0}{0}{1}{1}{1}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{0}{1}{1}{1}{0}{0}{line_break}"


class D(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{1}{1}{1}{0}{0}{0}{0}{line_break}" \
                                "{1}{0}{0}{1}{1}{0}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{1}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{1}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{1}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{1}{0}{line_break}" \
                                "{1}{0}{0}{1}{1}{0}{0}{line_break}" \
                                "{1}{1}{1}{0}{0}{0}{0}{line_break}"


class E(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "" \
                                "{1}{1}{1}{1}{1}{1}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{0}{line_break}" \
                                "{1}{1}{1}{1}{1}{1}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{0}{line_break}" \
                                "{1}{1}{1}{1}{1}{1}{0}{line_break}"


class F(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{1}{1}{1}{1}{1}{1}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{0}{line_break}" \
                                "{1}{1}{1}{1}{1}{0}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{0}{line_break}"


class G(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{0}{0}{1}{1}{1}{1}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{0}{1}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{0}{line_break}" \
                                "{1}{0}{1}{1}{1}{1}{1}{line_break}" \
                                "{1}{0}{0}{0}{1}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{1}{0}{0}{line_break}" \
                                "{0}{0}{1}{1}{1}{0}{0}{line_break}"


class H(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{1}{1}{1}{1}{1}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}"


class I(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{0}{1}{1}{1}{1}{1}{0}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}" \
                                "{0}{1}{1}{1}{1}{1}{0}{line_break}"


class J(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{0}{1}{1}{1}{1}{1}{1}{line_break}" \
                                "{0}{0}{0}{0}{1}{0}{0}{line_break}" \
                                "{0}{0}{0}{0}{1}{0}{0}{line_break}" \
                                "{0}{0}{0}{0}{1}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{1}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{1}{0}{0}{line_break}" \
                                "{0}{0}{1}{1}{1}{0}{0}{line_break}"


class K(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{1}{0}{0}{1}{0}{0}{line_break}" \
                                "{0}{1}{0}{1}{0}{0}{0}{line_break}" \
                                "{0}{1}{1}{0}{0}{0}{0}{line_break}" \
                                "{0}{1}{0}{1}{0}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{1}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}"


class L(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{0}{1}{0}{0}{0}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{0}{0}{line_break}" \
                                "{0}{1}{1}{1}{1}{1}{1}{line_break}"


class M(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{0}{0}{1}{0}{1}{0}{0}{line_break}" \
                                "{0}{0}{1}{0}{1}{0}{0}{line_break}" \
                                "{0}{1}{0}{1}{0}{1}{0}{line_break}" \
                                "{0}{1}{0}{1}{0}{1}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{1}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{1}{line_break}"


class N(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{1}{1}{0}{0}{1}{0}{line_break}" \
                                "{0}{1}{1}{0}{0}{1}{0}{line_break}" \
                                "{0}{1}{0}{1}{0}{1}{0}{line_break}" \
                                "{0}{1}{0}{1}{0}{1}{0}{line_break}" \
                                "{0}{1}{0}{0}{1}{1}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}"


class O(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{0}{0}{1}{1}{1}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{1}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{1}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{1}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{0}{1}{1}{1}{0}{0}{line_break}"


class P(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{0}{1}{1}{1}{0}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{1}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{1}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{1}{0}{0}{line_break}" \
                                "{0}{1}{1}{1}{0}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{0}{0}{line_break}"


class Q(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{0}{0}{0}{1}{1}{1}{0}{line_break}" \
                                "{0}{0}{1}{0}{0}{1}{0}{line_break}" \
                                "{0}{0}{1}{0}{0}{1}{0}{line_break}" \
                                "{0}{0}{1}{0}{0}{1}{0}{line_break}" \
                                "{0}{0}{0}{1}{1}{1}{0}{line_break}" \
                                "{0}{0}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{0}{0}{0}{0}{1}{0}{line_break}"


class R(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{0}{1}{1}{1}{0}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{1}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{1}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{1}{0}{0}{line_break}" \
                                "{0}{1}{1}{1}{0}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{1}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}"


class S(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{0}{0}{1}{1}{1}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{0}{0}{line_break}" \
                                "{0}{0}{1}{1}{1}{0}{0}{line_break}" \
                                "{0}{0}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{0}{1}{1}{1}{0}{0}{line_break}"


class T(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{1}{1}{1}{1}{1}{1}{1}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}"


class U(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{1}{0}{0}{0}{0}{0}{1}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{1}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{1}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{1}{line_break}" \
                                "{1}{0}{0}{0}{0}{1}{1}{line_break}" \
                                "{0}{1}{0}{0}{1}{0}{1}{line_break}" \
                                "{0}{0}{1}{1}{0}{0}{1}{line_break}"


class V(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{1}{0}{0}{0}{0}{0}{1}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{1}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{0}{1}{0}{1}{0}{0}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}"


class W(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{1}{0}{0}{0}{0}{0}{1}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{1}{line_break}" \
                                "{1}{0}{0}{1}{0}{0}{1}{line_break}" \
                                "{0}{1}{0}{1}{0}{1}{0}{line_break}" \
                                "{0}{1}{0}{1}{0}{1}{0}{line_break}" \
                                "{0}{1}{0}{1}{0}{1}{0}{line_break}" \
                                "{0}{0}{1}{0}{1}{0}{0}{line_break}"


class X(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{1}{0}{0}{0}{0}{0}{1}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{0}{1}{0}{1}{0}{0}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}" \
                                "{0}{0}{1}{0}{1}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{1}{0}{0}{0}{0}{0}{1}{line_break}"


class Y(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{1}{0}{0}{0}{0}{0}{1}{line_break}" \
                                "{0}{1}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{0}{1}{0}{1}{0}{0}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}"


class Z(Character):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string = "{1}{1}{1}{1}{1}{1}{1}{line_break}" \
                                "{0}{0}{0}{0}{0}{1}{0}{line_break}" \
                                "{0}{0}{0}{0}{1}{0}{0}{line_break}" \
                                "{0}{0}{0}{1}{0}{0}{0}{line_break}" \
                                "{0}{0}{1}{0}{0}{0}{0}{line_break}" \
                                "{0}{1}{0}{0}{0}{0}{0}{line_break}" \
                                "{1}{1}{1}{1}{1}{1}{1}{line_break}"
