def get_paths_generator(folders: list[str], path=()) -> list[str]:
    name, sub_folders = folders
    path = (*path, name)

    yield "/".join(path)

    for sub_folder in sub_folders:
        if isinstance(sub_folder, list):
            yield from get_paths_generator(sub_folder, path)
        else:
            yield "/".join((*path, sub_folder))



file_tree = [
    '',
    [
        [
            'etc',
            ['passwd', 'shadow']
        ],
        [
            'usr',
            [
                [
                    'bin', 
                    ['cat', 'ls']
                ],
                [
                    'lib',
                    [
                        'my_lib',
                        [
                            'gcc',
                            ['x86_64-linux-gnu']
                        ]
                    ]
                ]
            ]
        ]
    ]
]

print(list(get_paths_generator(file_tree)))