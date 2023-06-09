# Ansible

## Principes

Machine master se connecte en ssh sur les noeuds et pousse les progs (modules)

- playbook : appel les **rôles** et défini les **hosts** (noeuds)
- rôle : ensemble de tasks
- tasks : contient les modules

Le noeud maître se base sur un fichier *"inventaire"* qui fournit la liste des noeuds sur lesquels les playbook doivent être joués

- main.yml : contient les différentes tasks à appeler :

```yaml

- include_task : prerequisite.yml
- include_task : install.yml

```

## Fichier YAML

Commence toujours pas 3 tirets : ---

tâches : commence par un tiert : -<nomTâche>

Chauqe tâche utilise un module avec ses 2 arguments ou ses options. (mis à la ligne et décalé de 2 espaces)

souvent utilisation du nom **main.yml**
c'est l'arbo qui défini de quoi on parle

## Fichier de variable commun

ex

	 mediawiki/commun/defaults/main.yml

==> variable déclarée en type clé:valeur

ex :

	 db_user : "mediawiki"

Pour exploiter la variable, utiliser {{ }} + entre "" (string à chaque fois les valeurs?

ex :

```yaml

directory:"/apache/directory"
maintenance_dir:"{{directory}}/bak"

```

## Utilisation fichier var dans un autre fichier YAML

### 1/ déclarer la dépendance dans le fichier qui en a besoin. avec la tâhce "dependencies"

	mediawiki/meta/main.yml

EX du fichier :

```yaml
 ---
```

dependencies:

```yaml
  -role: "mediawiki/commun"
```

  ==> les fichiers sont organisés :
  XXXX/commun/defaults/main.xml
  XXXX/meta/main.xml
  XXXX/tasks/main.xml

## Structure d'un Playbook

- commence par 3 tirets
- bloc général
	- entête
		- nom des nodes ou groupe concernés, var, options
- bloc spécifiques (jeux d'instructions / *play*)
	- instruction
		- nom du jeu (tiret au début)
		- entête (optionnel)
		- section (tasls, rôles, handlers ...)

Chaque ligne à l'intérieur d'un bloc est indentée et chaque début de ligne décalé de 2 espaces.

playbook ==> liste de jeux d'instructions (play)

main.yml ==> liste de tasks ou variables