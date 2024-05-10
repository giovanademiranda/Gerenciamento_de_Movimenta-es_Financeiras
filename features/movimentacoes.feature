Feature: Gerenciamento de Movimentações Financeiras

  Scenario: Adicionar uma movimentação de crédito
    Given que estou na página inicial do Seu Barriga
    When eu adiciono uma movimentação de crédito de R$ 100,00
    Then eu devo ver a movimentação de crédito na lista de transações

  Scenario: Adicionar uma movimentação de débito
    Given que estou na página inicial do Seu Barriga
    When eu adiciono uma movimentação de débito de R$ 50,00
    Then eu devo ver a movimentação de débito na lista de transações
