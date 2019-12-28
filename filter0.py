      self.filter0 = []
      for i in a['12']:
          if i[1:-1] == '':
              self.filter0.append(set(i[1:-1]) & my_course == set())
          else:
              list1 = [int(j) for j in i[1:-1].split(',')]
              self.filter0.append(set(list1) & my_course == set())
