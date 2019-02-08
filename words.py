
class Word:
    emoji = None
    formatted_string = ''
    def __init__(self, emoji):
        self.emoji = emoji
    def print(self):
        return self.formatted_string.format(word=self.emoji)

class D(Word):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string="{word}    {word} \n\
{word}              {word} \n\
{word}                 {word} \n\
{word}              {word} \n\
{word}    {word}"

class E(Word):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string="{word}   {word}   {word} \n\
{word} \n\
{word}   {word}   {word} \n\
{word}  \n\
{word}   {word}   {word}"

class A(Word):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string="                  {word} \n\
         {word}          {word} \n\
     {word} {word}  {word} {word} \n\
  {word}                           {word} \n\
{word}                                {word}"

class L(Word):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string="{word}\n\
{word} \n\
{word} \n\
{word} \n\
{word} {word} {word} {word}"

class W(Word):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string="{word}                        {word}                         {word} \n\
    {word}              {word}   {word}                 {word} \n\
      {word}          {word}        {word}           {word} \n\
         {word}    {word}               {word}  {word} "

class I(Word):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string="{word}  {word}  {word} \n\
          {word} \n\
          {word} \n\
          {word} \n\
          {word} \n\
{word}  {word}  {word}"

class T(Word):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string="{word} {word} {word}  {word}  {word} \n\
                   {word} \n\
                   {word} \n\
                   {word} \n\
                   {word} \n\
                   {word}"

class H(Word):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)
        self.formatted_string="{word}                   {word} \n\
{word}                   {word} \n\
{word} {word} {word} {word} \n\
{word}                   {word} \n\
{word}                   {word}"