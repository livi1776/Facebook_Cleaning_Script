import re

if __name__ == '__main__':
  # Opens file - change File_name.txt to your filename
  with open('File_name.txt', "r") as rf:
    text = rf.read()
      # Removes extraneous text
      text = re.sub('\n','', text)
      text = re.sub('Like','', text)
      text = re.sub('Reply', '', text)
      text = re.sub('Write a comment…', '', text)
      text = re.sub('      *', '', text)
      text = re.sub('    *', '', text)
      text = re.sub('CommentsCommentCommentsView', '', text)

      # New file to store cleaned text
      with open('Copy_of_file_name.txt', "w") as wf:
          for line in text:
              wf.write(line)
