#make blocks that hold data in a class/structure
#make a array to hold the block making a chain

class block:
    def __init__(self, shaID, previousBlock):
        self.shaID = shaID  
        self.previousBlock = previousBlock
        self.nextBlock = "None"

if "__main__" == __name__:

    blockChain = []
    firstBlock = block("first block", "None")
    blockChain.append(firstBlock)

    def checkBlocks(blockIndex):
        try:
            if blockChain[blockIndex].previousBlock == "None":
                print("this is the first block")
                print(f"next Block ID {blockChain[blockIndex].nextBlock}")

                #checking right to left blocks
                if blockChain[blockIndex].shaID == blockChain[blockIndex+1].previousBlock:
                    print(f"chain is unbroken between {blockIndex} and {blockIndex+1} \n")
                    print(f"this block id:                 {blockChain[blockIndex].shaID}")
                    print(f"next block right pointer:      {blockChain[blockIndex+1].previousBlock}")
                else:
                    print(f"this block id:                {blockChain[blockIndex].shaID}")
                    print(f"next block right pointer:      {blockChain[blockIndex+1].previousBlock}")
                    print("chain is broken")  
                    print("======================================================\n")

                #left to right
                if hash(blockChain[blockIndex]) == blockChain[blockIndex].nextBlock:
                    print(f"chain is unbroken between {blockIndex+1} and {blockIndex} \n")
                    print(f"next block id:                {hash(blockChain[blockIndex])}")
                    print(f"this block left pointer:      {blockChain[blockIndex].nextBlock}\n")
                else:
                    print(f"next block id:                {hash(blockChain[blockIndex])}")
                    print(f"this block left pointer:      {blockChain[blockIndex].nextBlock}")
                    print("chain is broken")  
                    print("======================================================\n")    


            elif blockChain[blockIndex].nextBlock == "None":
                ######################################################################################
                #check last block
                print("this is the last block")
                print(f"previous Block ID {blockChain[blockIndex].previousBlock}")

                #this checks the left side of the last block
                if hash(blockChain[blockIndex-2]) == blockChain[blockIndex].previousBlock:
                    print(f"chain is unbroken between {blockIndex -1} and {blockIndex}")
                    print(f"previous block id:             {hash(blockChain[blockIndex-2])}")
                    print(f"this block left block pointer: {blockChain[blockIndex].previousBlock}")
                else:
                    print("chain is broken")  

                #this was a stupid bug so id i put [blockIndex-2].nextBlock it would get the previous id of the
                #last block i had to make the index one less then the searched index for it to work
                nb = blockIndex -1
                #this checks the right side of the second to last block
                if hash(blockChain[blockIndex-1]) == blockChain[nb].nextBlock:
                    print(f"chain is unbroken between {blockIndex -1} and {blockIndex} \n")
                    print(f"this block id:                {hash(blockChain[blockIndex-1])}")
                    print(f"previous block right pointer: {blockChain[nb].nextBlock:}")
                else:
                    print("chain is broken")  
                    print("======================================================\n")
                #####################################################################################
            else:
                print("this a inner block ")
                print(f"previous Block ID {blockChain[blockIndex].previousBlock}")
                print(f"next Block ID {blockChain[blockIndex].nextBlock}")
                
        except:
            print(f"no block at position {blockIndex}")

    
    def addNewBlock():
        resultID = hash(blockChain[len(blockChain)-1])
        newBlock = block(resultID, blockChain[len(blockChain)-1].shaID)
        blockChain.append(newBlock)

        blockChain[len(blockChain)-2].nextBlock = resultID
                                                           
    addNewBlock()
    addNewBlock()
    addNewBlock()

    print(len(blockChain))

    checkBlocks(0)
    #checkBlocks(1)
    checkBlocks(3)
    #checkBlocks(7)

    #print(hash(blockChain[1]))
    for b in blockChain:
        print("BlockID: -> " + str(b.shaID) + "\nLeftBlock: -> " + str(b.previousBlock) + "\nRightBlock: -> " + str(b.nextBlock))
        print("========================================================\n")