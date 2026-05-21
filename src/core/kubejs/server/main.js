ServerEvents.recipes(event => {
    event.recipes.createMechanicalCrafting('create_fantasizing:block_placer', [
        'AAABC',
        '  DEF'
    ], {
        A: 'create:sturdy_sheet',
        B: 'create:precision_mechanism',
        C: 'minecraft:beacon',
        D: 'minecraft:end_rod',
        E: 'create:andesite_alloy',
        F: 'create:brass_ingot',
    })
})