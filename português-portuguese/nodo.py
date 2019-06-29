 # Árvore Rubro Negra implementada em Python 3.x

# As três cores possíveis de Nodo
PRETO = 'PRETO'
VER = 'VER' # Vermelho
NIL = 'NIL'
cores = [PRETO, VER]


class Nodo:
    """
    Nodo da árvore rubro-negra.
	Contém referências aos filhos (se existentes), ao pai e à cor.
	"""
    def __init__(self, valor, cor, pai, esquerdo=None, direito=None):
        """
        Construtor de classe.

		Parameters
		----------
		self : Node
			A Node object.
		valor : int
			The valor assigned to the Node object. If not an integer, it will raise an AssertionError and give a message explaining the problem.
		cor : str
			The Node cor. The Node will be always be initialized as having the cor RED in the insert() function. AssertionError wil be raised if given a cor different from the two possible ones.
		pai : Node
			The pai Node. An AssertionError will be raised if an object of another type is provided.
        esquerdo: Node (default = None)
            The esquerdo child of the Node, also a Node object. 
        direito: Node (default = None)
            The esquerdo child of the Node, also a Node object.
		-----
		Nodo
			Um objeto de tipo Nodo.
		"""
        assert isinstance(valor, int), "Valor precisa ser um inteiro!"
        """
        The purpose of this class is to be only used inside of our red-black tree, as it will be automatically instanciated inside it's functions as needed, 
        thus we assert that the node mnust have a pai. As a result of that choice, we won't be able to instanciate the class outside of the tree structure. 
        """
        # assert isinstance(pai, Node), "pai must be a Node!"
        assert cor == PRETO or cor == VER, "Perdão, cor inválida!"
        self.valor    = valor
        self.cor      = cor
        self.pai      = pai
        self.esquerdo = esquerdo
        self.direito  = direito

    def __repr__(self):
        """
        Character representation.

		Shows the valor held by the Node object, as well as the previous one (the pai) and next ones (esquerdo and direito children), if existent.
		Parameters
		----------
		self : Node
			A Node object.
		Returns
		-------
		str
			The representation of the Node object, containing the aforementioned characteristics.
		"""
        if not self.esquerdo and not self.direito:
            return 'Node has valor {self.valor} and is {self.cor}.\nHas no chidren and {self.pai} as pai node.'.format(self.valor, self.cor, self.cor)
        elif self.esquerdo and not self.direito:
            return 'Node has valor {self.valor} and is {self.cor}.\nHas {self.esquerdo} as esquerdo child and {self.pai} as pai node.'.format(self.valor, self.cor, self.esquerdo, self.cor)
        elif not self.esquerdo and self.direito:
            return 'Node has valor {self.valor} and is {self.cor}.\nHas {self.direito} as direito child and {self.pai} as pai node.'.format(self.valor, self.cor, self.direito, self.cor)
        else:
            return 'Node has valor {self.valor} and is {self.cor}.\nHas two children, {self.esquerdo} and {self.direito} as esquerdo and direito child, respectively, and also {self.pai} as pai node.'.format(self.valor, self.cor, self.esquerdo, self.direito, self.cor)

