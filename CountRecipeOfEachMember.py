import math
def ocurrenceDivisionPlayers(aux, resultReceivers, quantityForPlayer):
    for i in range(len(aux)):    
        if aux[i] in resultReceivers:
            positionPlayer = resultReceivers.index(aux[i])
            quantityForPlayer[positionPlayer] = quantityForPlayer[positionPlayer]+1
        else:
            resultReceivers.append(aux[i])
            quantityForPlayer.append(1)


def audit(igneousPrice, countParties, resultReceivers, quantityForPlayer, quantityPlayersForParty, realValueForEachReceiver):
    totalOverflowCoinsByGroups = ((igneousPrice/quantityPlayersForParty) - math.floor(igneousPrice/quantityPlayersForParty))
    totalOverflow = countParties * totalOverflowCoinsByGroups * quantityPlayersForParty
    print("Coins Totais Excedentes: ", "*%ic*" % totalOverflow)
    print("Coins Totais Excedentes e auditados a dividir para todos os *%i* que estão no share: *%.3fc*" % (len(resultReceivers), totalOverflow/len(resultReceivers)))
    lastAcumulatedToShow = 0 
    if totalOverflow/len(resultReceivers) >= 1: 
        excceedToIncludeIShare = math.floor(totalOverflow/len(resultReceivers))
        print("Há coins que podem ser divididos entre todos os contemplados dessa leva, ou seja, todos os *%i* contemplados podem receber *%ic* extras" %(len(resultReceivers),excceedToIncludeIShare))
        print("\nContemplados(Quantidades que participou) = Lucro Final Individual")
        for i in range(len(resultReceivers)):
            lastAcumulatedToShow += realValueForEachReceiver[i]+excceedToIncludeIShare
            print("%s(%i) = *%ic*" %(resultReceivers[i],quantityForPlayer[i],realValueForEachReceiver[i]+excceedToIncludeIShare))    
        print("\nOBS.: Excedente do excedente fica com quem está pagando, pois não é possível outra divisão.")
        print("Total efetivamente dividido: *%ic*, Logo dos *%ic*, *%ic* é imposto ! 😋 " %(lastAcumulatedToShow, igneousPrice*countParties, excceedToIncludeIShare))
    else: 
        print("Valor excedente menor que o total de contemplados, logo não é possivel divisão entre todos !")
    

def showReceiversWithoutAudit(igneousPrice, countParties, resultReceivers, quantityForPlayer, quantityPlayersForParty):
    print("Unidade Igneous vendido a *%ic*" %(igneousPrice))
    print("Total de Igneous: *%i*" %countParties)
    print("Lucro Total: *%ic*" %(igneousPrice * countParties))
    
    for i in range(len(resultReceivers)):
        finalValueToReceive =  math.floor(igneousPrice/quantityPlayersForParty) * quantityForPlayer[i]
        print("%s(%i) = *%ic*" %(resultReceivers[i],quantityForPlayer[i],finalValueToReceive))
    print("\nValores auditados, conferidos e checados ! 😎")

def showReceiversWithAudit(igneousPrice, countParties, resultReceivers, quantityForPlayer, quantityPlayersForParty): 
    print("Unidade Igneous vendido a *%ic*" %(igneousPrice))
    print("Total de Igneous: *%i*" %countParties)
    print("Lucro Total: *%ic*" %(igneousPrice * countParties))
    acumulateFinalToCheck = 0
    realValueForEachReceiver = []
    for i in range(len(resultReceivers)):
        finalValueToReceive =  math.floor(igneousPrice/quantityPlayersForParty) * quantityForPlayer[i]
        realValueForEachReceiver.append(finalValueToReceive)
        acumulateFinalToCheck += finalValueToReceive

    print("\nAuditoria achou inconsistencias devido a impossiblidade de quebra em decimais dos coins ! 😡")
    print("Coins Totais Recebidos: *%ic*" %(igneousPrice * countParties))
    print("Valor total inteiro a dividir entre os contemplados: *%ic*" %acumulateFinalToCheck)
    audit(igneousPrice, countParties, resultReceivers, quantityForPlayer, quantityPlayersForParty, realValueForEachReceiver)
        
    
def needToBeAudited(igneousPrice, countParties, resultReceivers, quantityForPlayer, quantityPlayersForParty):
    if igneousPrice % quantityPlayersForParty == 0:
        showReceiversWithoutAudit(igneousPrice, countParties, resultReceivers, quantityForPlayer, quantityPlayersForParty)
    else:
        showReceiversWithAudit(igneousPrice, countParties, resultReceivers, quantityForPlayer, quantityPlayersForParty)


def entrance():  
    igneousPrice = int(input())
    parties = ''
    resultReceivers = []
    quantityForPlayer = []
    countParties = 0
    quantityPlayersForParty = 0
    defaultPartyQuantity = 6
    while parties != "END":
        parties = str(input())
        aux = parties.split(", ")
        if parties != "END":         
            countParties += 1 
            ocurrenceDivisionPlayers(aux, resultReceivers, quantityForPlayer)
            quantityPlayersForParty = len(aux)
    
    if quantityPlayersForParty == defaultPartyQuantity:
        needToBeAudited(igneousPrice, countParties, resultReceivers, quantityForPlayer, quantityPlayersForParty)
    else:
        print("Por favor verifique se todas as pt's possuem a mesma qtd de membros")

entrance()
