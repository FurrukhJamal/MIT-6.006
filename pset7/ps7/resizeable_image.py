import imagematrix
import math 

class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self):
        print(f"self.width : {self.width}")
        DP = {}
        for i in range(self.width):
            DP[i, 0] = self.energy(i, 0)

        Parents = {}
        for j in range(1, self.height):
            for i in range(self.width):
                # print(f"j : {j} i : {i}")
                DP[i, j] = self.energy(i, j) + DP[i, j - 1]
                Parents[i,j] = 0
                if i != 0:
                    if (DP[i, j] > self.energy(i, j ) + DP[i - 1, j - 1]):
                        DP[i,j] =  self.energy(i, j) + DP[i - 1, j - 1]
                        Parents[i,j] = -1
                if i != self.width - 1:
                    if DP[i , j] > self.energy(i, j ) + DP[i + 1, j - 1]:
                        DP[i , j] = self.energy(i, j ) + DP[i + 1, j - 1]
                        Parents[i, j] = 1
        # getting the best bottom pixel with the least energy
        
        bestMin = math.inf
        
        for i in range(self.width):
            if DP[i, self.height - 1] < bestMin:
                bestMin = DP[i, self.height - 1]
                index = i
        
        line = []
        for j in range(self.height - 1, 0, -1):
            line.append((index, j))
            index = index + Parents[index, j]
        line.append((index, 0))
        return line


        print(f"DP : {DP}")            
            

        # raise NotImplemented

    def remove_best_seam(self):
        self.remove_seam(self.best_seam())
